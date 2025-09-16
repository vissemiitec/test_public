import java.sql.*;

public class UnsafeAuthA {
    public boolean login(Connection conn, String username, String password) throws SQLException {
        // 直接拼接 user input -> 易受 SQL injection
        String sql = "SELECT id FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
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
