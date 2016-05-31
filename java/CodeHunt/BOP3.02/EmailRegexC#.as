using System.Text.RegularExpressions;
using System;

public static class Program {
    public static bool Puzzle(string s) {
        string validEmailPattern = @"^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$";
        return (new Regex(validEmailPattern, RegexOptions.IgnoreCase)).IsMatch(s);
    }
}