import streamlit as st

st.header("Questions:")

math_questions_list_easy = {
    1:[
        "What is the rank of the following 2x3 matrix?\n| 1  2  3 |\n| 4  5  6 |",
        ["A) 2", "B) 3", "C) 1", "D) 0"],
        "A"
    ],
    2:[
        "Which of the following is an example of a scalar in linear algebra?",
        ["A) A vector", "B) A matrix", "C) A real number", "D) A complex number"],
        "C"
    ],
    3:[
        "What is the trace of a 3x3 identity matrix?",
        ["A) 3", "B) 0", "C) 1", "D) 2"],
        "A"
    ],
    4:[
        "In a matrix multiplication AB, if A is an m x n matrix and B is an n x p matrix, what is the size of the resulting matrix AB?",
        ["A) m x p", "B) n x n", "C) p x m", "D) n x m"],
        "A"
    ],
    5:[
        "The determinant of a 2x2 matrix [a b; c d] is calculated as:",
        ["A) ad - bc", "B) ac - bd", "C) ab - cd", "D) bc - ad"],
        "A"
    ],
}
math_questions_list_hard={
    1: [
        "Question: What is the determinant of a 3x3 matrix with the following entries?\n| 2  0  1 |\n| 3  1 -2 |\n| 4  3  5 |",
        ["A) -26", "B) 26", "C) 34", "D) -34"],
        "A"
    ],
    2: [
        "Question: Which of the following matrices is not invertible (i.e., has no inverse)?",
        ["A) Identity matrix (3x3)", "B) A matrix with all elements equal to zero", "C) A matrix with all elements equal to one", "D) A matrix with zero determinant"],
        "D"
    ],
    3: [
        "Question: The eigenvectors of a matrix are linearly independent when:",
        ["A) They are orthogonal to each other", "B) They have different eigenvalues", "C) They are linearly dependent", "D) None of the above"],
        "B"
    ],
    4: [
        "Question: Which of the following operations changes the rank of a matrix?",
        ["A) Adding a multiple of one row to another row", "B) Multiplying all elements in a row by a non-zero constant", "C) Swapping two rows", "D) None of the above"],
        "D"
    ],
    5: [
        "Question: The transpose of a row matrix results in a:",
        ["A) Row matrix", "B) Column matrix", "C) Diagonal matrix", "D) Square matrix"],
        "B"
    ],
}



easy_crct = 0
hard_crct = 0
easy_wrng = 0
hard_wrng = 0

easy_question_index = 1
hard_question_index = 1

while easy_crct + easy_wrng < len(math_questions_list_easy) or hard_crct + hard_wrng < len(math_questions_list_hard):
    if easy_question_index <= len(math_questions_list_easy) and (easy_crct < 2 or (easy_crct - easy_wrng) < 1):
        question = math_questions_list_easy[easy_question_index]
        question_type = "easy"
    else:
        question = math_questions_list_hard[hard_question_index]
        question_type = "hard"

    st.write(question[0])
    ans = st.radio("Select an option:", question[1])

    st.write("You selected:", ans)

    if st.button("Submit"):
        correct_answer = question[-1]
        if ans[0] == correct_answer:
            if question_type == "easy":
                easy_crct += 1
            else:
                hard_crct += 1
        else:
            if question_type == "easy":
                easy_wrng += 1
            else:
                hard_wrng += 1

        if question_type == "easy":
            easy_question_index += 1
        else:
            hard_question_index += 1

st.write("Easy Questions - Correct:", easy_crct, "Wrong:", easy_wrng)
st.write("Hard Questions - Correct:", hard_crct, "Wrong:", hard_wrng)
