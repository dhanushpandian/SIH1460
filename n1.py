
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI




import streamlit as st
def create_template():
    template="""
    You are an expert quiz maker for technical fields.
    Create a quizz with {num_questions} multiple-choice questions about the following concepts {quiz_context} and increase the difficulty if i answer correctly and decrese if i answer wrong"""
    promt=PromptTemplate.from_template(template)
    promt.format(num_questions=10,quiz_context="python")
    return(promt)
def create_chain(prompt_template,llm):
    return LLMChain(llm=llm,prompt=prompt_template)
def main():
    st.title("Quiz App")
    st.write("Generates quiz")
    prompt_template=create_template()
    llm=ChatOpenAI(openai_api_key="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")
    chain=create_chain(prompt_template,llm)
    context=st.text_area("enter the contents of the quiz")
    num_questions=st.number_input("Enter number of inputs")
    if st.button("generate Quiz"):
        quiz_response=chain.run(num_questions=num_questions,quiz_context=context)
        st.write(quiz_response)
       
       
if __name__=="__main__":
    main()