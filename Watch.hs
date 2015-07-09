{-# LANGUAGE OverloadedStrings #-} -- for FilePath literals

import System.FSNotify
import Control.Concurrent (threadDelay)
import Control.Monad (forever)
import Filesystem.Path.CurrentOS
import System.Process
import Prelude hiding (FilePath)


sourceDir = "md/slides"
targetHtmlDir = "rbuild"
targetTexDir = "latex/slides"


revealCommand infile outfile =
  "pandoc -t revealjs " ++ encodeString infile ++ " -o " ++ encodeString outfile ++ " --no-highlight --template md/template.html -s"

toRevealName file = targetHtmlDir </> addExtension (basename file) "html"

texCommand infile outfile =
  "pandoc -t beamer " ++ encodeString infile ++ " -o " ++ encodeString outfile

toTexName file = targetTexDir </> addExtension (basename file) "tex"


build :: Event -> IO ()
build e =
  case e of
    (Added file _) -> action file
    (Modified file _) -> action file
    _ -> return ()
  where
    action file = do
      let revealName = toRevealName file
      let texName = toTexName file
      putStrLn $ "compiling file '" ++ encodeString file ++ "' to html file '" ++ encodeString revealName ++ "'"
      callCommand $ revealCommand file revealName
      putStrLn $ "compiling file '" ++ encodeString file ++ "' to tex file '" ++ encodeString texName ++ "'"
      callCommand $ texCommand file texName

main =
  withManager $ \mgr -> do
    -- start a watching job (in the background)
    watchDir
      mgr          -- manager
      sourceDir          -- directory to watch
      (flip hasExtension "md" . eventPath) -- predicate
      build        -- action

    -- sleep forever (until interrupted)
    forever $ threadDelay maxBound
