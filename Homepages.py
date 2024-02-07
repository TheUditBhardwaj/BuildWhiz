import streamlit as st
import datetime
import firebase_admin
import google_auth_httplib2
user_data = {}

st.set_page_config(
    page_title = "Login Page" ,
		page_icon="💻" ,
        layout = "wide"   
    )
st.title('Welcome to :violet[BuildWhiz] :sunglasses:')



st.title(" ")
st.title(" ")
st.title(" ")
def about():

  col1,col2 = st.columns(2)

  with col1:

    st.title('')
    st.title('')
    st.title('')


    st.subheader('''Many   of   you   must be knowing that selecting the best and affordable components which matches best with the other components is very difficult Our application helps the user to select the best and most efficient component for their system
    ''')
    
    st.subheader("  ")

    st.subheader("  In summary, component selection requires research, compatibility consideration, budget management, and staying updated on technology, all while aligning with your specific needs and skill level.  ")
    
    
  with col2:
    st.image(["BuildWhiz/BuildWhiz-3.png"],width=600)
    
    



    st.title(":green[Developed by :] ")
    st.header(":gray[BE YOU Developers]")
    st.subheader(" ",divider='rainbow')
    
    st.header(' :red[Our Team]')
    st.subheader("Udit Bhardwaj ")
    st.subheader("Kritika Dawar")
    st.subheader("Hardik  ")
    
  
def account(): 
  
  

  # Sign-Up Page
  def signup():
      col1,col2=st.columns(2)
      with col1:  
        st.title("Sign Up")
        new_name= st.text_input("Enter a Name ")
        new_username = st.text_input("Create a username")
        new_password = st.text_input("Create a password", type="password")
        

      if st.button("Sign Up"):
          if new_username and new_password:
              user_data[new_username] = new_password
              st.success("You have successfully signed up! Please log in.")
              
          
            
          else:
              st.error("Username and password are required.")
      

  # Login Page
  def login():
        
        col1,col2=st.columns(2)
        
        with col1:

            st.title("Login")
            name = st.text_input("Name")
            username = st.text_input("Username")
            password = st.text_input("Password",type="password")

        if st.button("Login"):
            if username in user_data and user_data[username] ==password:
                st.success(f"Welcome, {username}!")
            elif username=='user@gmail.com' and password =='helloworld':
                st.header(" :violet[Welcome,]",name)
            
                about()
            
            elif username=='udit@gmail.com' and password =='udit123':
                st.header(" :violet[Welcome,]",name)
                about()
            
            
            else:
                st.error("Incorrect username or password. Please try again.")

  # Main application
  def main():
        st.header("Login and Sign Up App")
        st.subheader("Choose an option:")
        st.subheader("")
        st.subheader("")
        option = st.selectbox("Select an option", [ "Sign Up","Login"])

        if option == "Login":
            login()
        elif option == "Sign Up":
            signup()

  if __name__ == '__main__':
      main()


account()
      
    
    



