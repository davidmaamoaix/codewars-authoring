module ConcatMeSpec where

import Test.Hspec
import Text.Printf

import ConcatMe

foldConcat :: [[a]] -> [a]
foldConcat = foldr (foldr p q) r

-- concatTest :: (Eq a, Show a) => [[a]] -> SpecWith ()
concatTest xs = describe (show xs) $ do
  it (printf "should return %s given %s as input" (show $ concat xs) (show xs)) $ do
        foldConcat xs `shouldBe` concat xs

spec :: Spec
spec = do
  describe "Fold Some Lists" $ do
    concatTest [[1], [2], [3], [4], [5]]
    concatTest ["Hello", " ", "World", "!"]
    concatTest [[1, 2, 3], [2, 3], [9, 10]]
    concatTest [[[-10, 23], [6, 7, 9], []], [[1, 2, 3]]]
    concatTest ["M", "a", "d", "e", " ", "i", "n", " ", "h", "e", "a", "v", "e", "n"]
  describe "Empty Boi" $ do
    describe ("[]") $ do
      it (printf "Empty [Int]") $ do (foldConcat [] :: [Int]) `shouldBe` []
      it (printf "Empty [String]") $ do (foldConcat [] :: [String]) `shouldBe` []
      it (printf "Empty [[Int]]") $ do (foldConcat [] :: [[Int]]) `shouldBe` []
    concatTest [""]
    concatTest ["", "", ""]
