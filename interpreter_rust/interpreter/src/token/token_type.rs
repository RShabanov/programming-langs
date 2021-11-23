#[derive(Debug, PartialEq)]
pub enum TokenType {
    Integer,
    Float,
    Add,
    Sub,
    Mul,
    Div,
    Pow,
    Lp, // Left Parenthesis
    Rp, // Right Parenthesis
    Eos,
}