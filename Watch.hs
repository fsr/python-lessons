{-# LANGUAGE OverloadedStrings #-} -- for FilePath literals

import System.FSNotify
import Control.Concurrent (threadDelay)
import Control.Monad (forever)
import Filesystem.Path.CurrentOS
import Filesystem
import System.Process
import Prelude hiding (FilePath)
import System.Environment
import Text.Printf


sourceDir = "md/slides"
targetHtmlDir = "rbuild"
targetTexDir = "latex/slides"
fileFilter = flip hasExtension "md"


revealCommand =
  printf "pandoc -t revealjs %s -o %s --no-highlight --template md/template.html -s"

toRevealName file = targetHtmlDir </> addExtension (basename file) "html"

texCommand =
  printf "pandoc -t beamer %v -o %v"

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
  putStrLn $ printf "compiling $ html '%v' -> '%v'" fileName revealName
  callCommand $ revealCommand fileName revealName
  putStrLn $ printf "compiling $ tex '%v' -> '%v'" fileName texName
  callCommand $ texCommand fileName texName
  where
    fileName  = encodeString file
    revealName = encodeString $ toRevealName file
    texName    = encodeString $ toTexName file


main :: IO ()
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
