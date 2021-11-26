use super::token::{Token, TokenType};

#[derive(Debug)]
pub(crate) struct Lexer {
    position: usize,
    text: Vec<char>
}

impl Lexer {
    pub fn from<'a>(text: &'a str) -> Self {
        Self {
            position: 0,
            text: text.chars().collect()
        }
    }

    pub fn next(&mut self) -> Token {
        while let Some(current_char) = self.text.get(self.position) {
            if current_char.is_whitespace() {
                self.skip();
                continue;
            }

            if current_char.is_ascii_digit() {
                return self.number();
            } else {
                self.position += 1;

                let token_type = match current_char {
                    '+' => TokenType::Add,
                    '-' => TokenType::Sub,
                    '*' => TokenType::Mul,
                    '/' => TokenType::Div,
                    '^' => TokenType::Pow,
                    '(' => TokenType::Lp,
                    ')' => TokenType::Rp,
                    _ => panic!("Undefined token {:?}", current_char)
                };

                return Token::new(token_type, Some(current_char.to_string()));
            }
        }
        return Token::new(TokenType::Eos, None);
    }

    fn skip(&mut self) {
        while let Some(current_char) = self.text.get(self.position) {
            if !current_char.is_whitespace() {
                break;
            }
            self.position += 1;
        }
    }

    fn number(&mut self) -> Token {
        let mut integer_part = self.integer();

        if let Some(current_char) = self.text.get(self.position) {
            if current_char == &'.' {
                integer_part.push(*current_char);
                self.position += 1;
                let float_part = self.integer();

                return Token::new(TokenType::Float, Some(integer_part + &float_part));
            }
        }

        Token::new(TokenType::Integer, Some(integer_part))
    }

    fn integer(&mut self) -> String {
        let mut number = Vec::<char>::new();

        while let Some(current_char) = self.text.get(self.position) {
            // for now we use only decimal numbers
            if !current_char.is_ascii_digit() {
                break;
            }

            number.push(*current_char);
            self.position += 1;
        }

        number.into_iter().collect::<String>()
    }
}


#[cfg(test)]
mod tests {
    use super::{Lexer, Token, TokenType};

    #[test]
    fn create_lexer_from() {
        let mut lexer = Lexer::from("2 + 5");
        assert_eq!("Lexer { position: 0, text: ['2', ' ', '+', ' ', '5'] }", format!("{:?}", lexer));

        lexer = Lexer::from(&String::from("2 + 5"));
        assert_eq!("Lexer { position: 0, text: ['2', ' ', '+', ' ', '5'] }", format!("{:?}", lexer));
    }

    #[test]
    fn tokenize() {
        let mut lexer = Lexer::from("4 - 5");

        let lhs = Token::new(TokenType::Integer, Some("4".to_string()));
        let mut token = lexer.next();
        assert_eq!(lhs, token);

        let op = Token::new(TokenType::Sub, Some("-".to_string()));
        token = lexer.next();
        assert_eq!(op, token);

        let rhs = Token::new(TokenType::Integer, Some("5".to_string()));
        token = lexer.next();
        assert_eq!(rhs, token);
    }

    #[test]
    fn tokenize_empty_str() {
        let mut lexer = Lexer::from("");
        let empty_token = Token::new(TokenType::Eos, None);
        
        assert_eq!(empty_token, lexer.next());
    }
}