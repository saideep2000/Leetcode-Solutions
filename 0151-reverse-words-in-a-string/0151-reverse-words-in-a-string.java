class Solution {
    public String reverseWords(String s) {
        String[] rec = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for(int i=(rec.length)-1; i >= 0; i--){
            sb.append(rec[i]);
            sb.append(" ");
        }
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }
}