package io.duck;

public class RabinKarp {
  public int search(String text, String pattern) {
    int alphabetSize = 256;
    int primeNum = 101;
    int patternHash = 0;
    int textHash = 0;
    int firstIndexHash = 1;
    int countOfmatches = 0;

    for (int i = 0; i < pattern.length() - 1; i++) {
      firstIndexHash = (firstIndexHash * alphabetSize) % primeNum;
    }

    for (int i = 0; i < pattern.length(); i++) {
      patternHash = (alphabetSize * patternHash + pattern.charAt(i)) % primeNum;
      textHash = (alphabetSize * textHash + text.charAt(i)) % primeNum;
    }

    for (int i = 0; i <= text.length() - pattern.length(); i++) {
      if (patternHash == textHash) {
        int counter = 0;
        for (int j = 0; j < pattern.length(); j++) {
          counter++;
          if (text.charAt(i + j) != pattern.charAt(j))
            break;
        }

        if (counter == pattern.length()) {
          countOfmatches++;
        }
      }

      if (i < text.length() - pattern.length()) {
        textHash = (alphabetSize * (textHash - text.charAt(i) * firstIndexHash) + text.charAt(i + pattern.length())) % primeNum;

        if (textHash < 0) {
          textHash = (textHash + primeNum);
        }
      }
    }
    return countOfmatches;
  }
}
