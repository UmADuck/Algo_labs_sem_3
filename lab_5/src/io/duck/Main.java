package io.duck;

public class Main {
  public static void main(String[] args) {
    RabinKarp rabinKarp = new RabinKarp();
    String txt = "Salo Salo Salo salo Salo";
    String pat = "Salo";
    System.out.printf("%s%d", "Count of matches: ", rabinKarp.search(txt, pat));
  }
}
