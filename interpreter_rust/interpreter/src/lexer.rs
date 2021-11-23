use super::token::{Token, TokenType};

#[derive(Debug)]
pub(crate) struct Lexer {
    position: usize,
    text: String,
}

impl Lexer {
    pub fn new(text: String) -> Self {
        Self {
            position: 0,
            text: text
        }
    }

    pub fn from(text: &str) -> Self {
        Lexer::new(text.to_string())
    }

    pub fn next(&mut self) -> Token {
        while let Some(current_char) = self.text.chars().nth(self.position) {
            if current_char == ' ' {
                self.skip();
                continue;
            }

            if current_char.is_ascii_digit() {
                let (token_type, number) = self.number();
                return Token::new(token_type, Some(number));
            } else {
                let current_char = current_char.to_string();
                self.forward();

                match current_char.as_str() {
                    "+" => return Token::new(TokenType::Add, Some(current_char)),
                    "-" => return Token::new(TokenType::Sub, Some(current_char)),
                    "*" => return Token::new(TokenType::Mul, Some(current_char)),
                    "/" => return Token::new(TokenType::Div, Some(current_char)),
                    "^" => return Token::new(TokenType::Pow, Some(current_char)),
                    "(" => return Token::new(TokenType::Lp, Some(current_char)),
                    ")" => return Token::new(TokenType::Rp, Some(current_char)),
                    _ => panic!("Undefined token {:?}", current_char)
                }
            }
        }
        return Token::new(TokenType::Eos, None);
    }

    fn forward(&mut self) {
        self.position += 1;
    }

    fn skip(&mut self) {
        let space = Some(' ');
        while self.text.chars().nth(self.position) == space {
            self.forward();
        }
    }

    fn integer(&mut self) -> String {
        let mut number = Vec::<char>::new();
        let mut current_char = self.text.chars().skip(self.position);

        while let Some(current_char) = current_char.next() {
            if !current_char.is_ascii_digit(){
                break;
            }

            number.push(current_char);
            self.position += 1;
        }

        number.into_iter().collect::<String>()
    }

    fn number(&mut self) -> (TokenType, String) {
        let mut integer_part = self.integer();

        if let Some(current_char) = self.text.chars().nth(self.position) {
            if current_char == '.' {
                integer_part.push(current_char);
                self.forward();
                let float_part = self.integer();

                return (TokenType::Float, integer_part + &float_part);
            }
        }
        (TokenType::Integer, integer_part)
    }
}

#[cfg(test)]
mod tests {
    use super::{Lexer, Token, TokenType};

    #[test]
    fn create_lexer_from() {
        let lexer = Lexer::from("2 + 5");
        assert_eq!("Lexer { position: 0, text: \"2 + 5\" }", format!("{:?}", lexer));
    }

    #[test]
    fn create_lexer_new() {
        let lexer = Lexer::new("2 + 5".to_string());
        assert_eq!("Lexer { position: 0, text: \"2 + 5\" }", format!("{:?}", lexer));
    }

    #[test]
    fn tokenize() {
        let mut lexer = Lexer::from("2 + 5");

        let lhs = Token::new(TokenType::Integer, Some("2".to_string()));
        let mut token = lexer.next();
        assert_eq!(lhs, token);

        let op = Token::new(TokenType::Add, Some("+".to_string()));
        token = lexer.next();
        assert_eq!(op, token);

        let rhs = Token::new(TokenType::Integer, Some("5".to_string()));
        token = lexer.next();
        assert_eq!(rhs, token);
    }
}