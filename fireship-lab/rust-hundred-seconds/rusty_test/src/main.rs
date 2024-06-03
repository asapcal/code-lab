fn main() {
    println!("Hi, you all, my favorite number follows bellow.");
    let /*mut*/ hello: Vec<i32> = (0..11).collect();

    fn do_stuff(val: &Vec<i32>) {
        println!("{}", val.len() );
    }

    do_stuff(&hello)
}
