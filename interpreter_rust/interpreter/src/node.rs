use super::token::Token;

#[derive(Debug)]
pub(crate) enum Node {
    Number(Token),
    BinOp(Box<Node>, Token, Box<Node>),
    UnaryOp(Token, Box<Node>),
}