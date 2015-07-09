{-# LANGUAGE OverloadedStrings #-} -- for FilePath literals

import System.FSNotify
import Control.Concurrent (threadDelay)
import Control.Monad (forever)
import Filesystem.Path.CurrentOS
import Filesystem
import System.Process
import Prelude hiding (FilePath)
import System.Environment


sourceDir = "md/slides"
targetHtmlDir = "rbuild"
targetTexDir = "latex/slides"
fileFilter = flip hasExtension "md"


revealCommand infile outfile =
  "pandoc -t revealjs " ++ encodeString infile ++ " -o " ++ encodeString outfile ++ " --no-highlight --template md/template.html -s"

toRevealName file = targetHtmlDir </> addExtension (basename file) "html"

texCommand infile outfile =
  "pandoc -t beamer " ++ encodeString infile ++ " -o " ++ encodeString outfile

toTexName file = targetTexDir </> addExtension (basename file) "tex"


buildEvent :: Event -> IO ()
buildEvent e =
  case e of
    (Added file _) -> build file
    (Modified file _) -> build file
    _ -> return ()
  where


build :: FilePath -> IO ()
build file = do
  let revealName = toRevealName file
  let texName = toTexName file
  putStrLn $ "compiling file '" ++ encodeString file ++ "' to html file '" ++ encodeString revealName ++ "'"
  callCommand $ revealCommand file revealName
  putStrLn $ "compiling file '" ++ encodeString file ++ "' to tex file '" ++ encodeString texName ++ "'"
  callCommand $ texCommand file texName

main = do
  args <- getArgs
  case args of
    [] -> watch
    ["watch"] -> watch
    ["compile"] -> compile
    [_] -> error "wrong command line arguments"
    _ -> error "wrong number of arguments (expected 0 or 1)"
  where
    compile = do
      allFiles <- listDirectory sourceDir
      mapM_ build $ filter fileFilter allFiles
    watch = do
      compile
      withManager $ \mgr -> do
        watchDir
          mgr
          sourceDir
          (fileFilter . eventPath)
          buildEvent
        forever $ threadDelay maxBound
