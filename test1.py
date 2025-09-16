# 不安全示範：直接把未經處理的使用者輸入拼到 SQL 會導致 SQL injection
def unsafe_login(conn, username: str, password: str) -> bool:
    # 直接拼接 user input -> 易受 SQL injection
    sql = "SELECT id FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row is not None
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass

