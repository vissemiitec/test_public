package com.example;

import java.sql.*;

public class UnsafeAuthExample {

    // 不安全登入（SQL Injection 範例）
    public boolean loginUnsafe(Connection conn, String username, String password) throws SQLException {
        String sql = "SELECT id FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            return rs.next();
        }
    }

    // 安全登入（PreparedStatement 範例）
    public boolean loginSafe(Connection conn, String username, String password) throws SQLException {
        String sql = "SELECT id FROM users WHERE username = ? AND password = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, username);
            pstmt.setString(2, password);
            try (ResultSet rs = pstmt.executeQuery()) {
                return rs.next();
            }
        }
    }

    // 呼叫端 context，模擬從外部輸入
    public static void main(String[] args) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:h2:mem:testdb", "sa", "");
        UnsafeAuthExample auth = new UnsafeAuthExample();

        String username = args.length > 0 ? args[0] : "admin";
        String password = args.length > 1 ? args[1] : "1234";

        auth.loginUnsafe(conn, username, password);
        auth.loginSafe(conn, username, password);
    }
}
