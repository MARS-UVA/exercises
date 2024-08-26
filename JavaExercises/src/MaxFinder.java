public class MaxFinder {
    public static int max(int a, int b, int c) {
        if (a > b) {
            if (c < b) {
                return a;
            }
            else {
                return c;
            }
        }
        else {
            if (b > c) {
                return b;
            }
        }
        return c;
    }
}
