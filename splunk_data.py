// 範例 A：不安全登入（切勿在生產環境使用） // 目的：示範把未經處理的輸入直接拼到 SQL 中 import java.sql.*;
public class UnsafeAuthA {
    public boolean login(Connection conn, String username, String password) throws SQLException {
        // 直接拼接 user input -> 易受 SQL injectionString sql = "SELECT id FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
        Statement stmt = null;
        ResultSet rs = null;
        try {
            stmt = conn.createStatement();
            rs = stmt.executeQuery(sql);
            return rs.next();
        } finally {
            if (rs != null) try { rs.close(); } catch (Exception e) {}
            if (stmt != null) try { stmt.close(); } catch (Exception e) {}
        }
    }
}
