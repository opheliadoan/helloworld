import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
}

class check_brackets {
    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();

        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        Bracket cur;
        int wrong_occurence = 0;
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);

            if (next == '(' || next == '[' || next == '{') {
                // Process opening bracket, write your code here
                cur = new Bracket(next, position);
                opening_brackets_stack.push(cur);
            }

            if (next == ')' || next == ']' || next == '}') {
                // Process closing bracket, write your code here
                if(opening_brackets_stack.empty()) {
                    System.out.println(position + 1);
                    return;
                }
                cur = opening_brackets_stack.pop();
                if (!cur.Match(next)) {
                    wrong_occurence = position + 1;
                    System.out.println(wrong_occurence);
                    return;
                }
            }
        }

        // Printing answer, write your code here
        if(!opening_brackets_stack.empty()) {
            while(!opening_brackets_stack.empty()) {
                wrong_occurence = opening_brackets_stack.pop().position + 1;
            }
            System.out.println(wrong_occurence);
        } else {
            System.out.println("Success");
        }

    }
}
