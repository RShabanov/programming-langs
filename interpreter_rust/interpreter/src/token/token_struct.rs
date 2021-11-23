use super::token_type::TokenType;

#[derive(Debug, PartialEq)]
pub struct Token {
    pub token: TokenType,
    pub value: Option<String>
}

impl Token {
    pub fn new(token: TokenType, value: Option<String>) -> Self {
        Self {
            token,
            value
        }
    }
}

#[cfg(test)]
mod tests {
    use super::{TokenType, Token};

    #[test]
    fn create_token() {
        Token::new(TokenType::Integer, Some("4".to_string()));
    }

    #[test]
    fn cmp_tokens() {
        let lhs_token = Token::new(TokenType::Integer, Some("4".to_string()));
        let mut rhs_token = Token::new(TokenType::Integer, Some("4".to_string()));

        assert_eq!(lhs_token, rhs_token);

        rhs_token = Token::new(TokenType::Float, Some("2".to_string()));
        assert_ne!(lhs_token, rhs_token);
    }
}