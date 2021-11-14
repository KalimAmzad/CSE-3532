import streamlit as st

# st.title("Image Portal | All in One")
st.title("Data Science Bootcamp Registration")

st.write("A part of course word CSE-3532")


user_choice = st.sidebar.selectbox('Your choice', ('', 'Code', 'Sytem Interaction'))

if user_choice == 'Code':
	st.code('''import streamlit as st

	st.title("Image Portal | All in One")
	st.write("A part of course word CSE-3532")

	st.write("To install all required packages plz use the following command")
	st.code("pip install -r requirements.txt")''')

elif user_choice == 'Sytem Interaction':
	st.write("Greetings!! You are now interacting with the system")


def calculate_eligibility(per_week_hour, start_date, end_date, institution='IIUC'):
	weighted_point = 0

	if per_week_hour >= 3:
		weighted_point += (per_week_hour*1.5)

	if institution == 'IIUC':
		weighted_point += 7

	# if start_date >= '2021-10-14' and end_date <= '2021-10-24':
	# 	weighted_point += 15

	return weighted_point, institution

# learning_level = st.sidebar.multiselect('Select your Learning Level', ['Beginner', 'Intermediate', 'Advanced'])
# st.write(learning_level)

# semesters = st.sidebar.multiselect('Select your Semester', list(range(1, 9)))
# st.write(semesters)


start_date = st.date_input("When you want to start your Bootcamp?")
end_date = st.date_input("When you want to complete your Bootcamp?")
st.write(start_date)

name = st.text_input("Name")
email = st.text_input("E-mail")
institution = st.text_input("Institution")
mobile = st.number_input("Mobile Number (01XXXXXX)")
address = st.text_area("Address")
per_week_hour = st.slider("How many hours you can give per week", min_value=2, max_value=10)
gender = st.radio('Gender', ('Male', 'Female'))

submit_result = st.button("Submit")


if submit_result:
	# calculate the eligibility of the candidate to be selected at Bootcamp

	st.write(f'Hi *{name}*\n Following is your eligibility score')

	weighted_point, institution = calculate_eligibility(per_week_hour, start_date, end_date, institution)

	if weighted_point >= 15:
		st.success(f"You are eligible for our Premium Batch at your selected date {start_date} -- {end_date}")
	elif weighted_point >= 10:
		st.success(f"You are eligible for our Silver Batch at your selected date {start_date} -- {end_date}") 
	else:
		st.warning("Try next time please")


# for s in semesters:
# 	if s == 1:
# 		weighted_point += 3
# 	elif s == 2:
# 		weighted_point += 5
# 	elif s == 3:
# 		weighted_point += 7
# 	else:
# 		weighted_point += 10

# st.write(f'Hi, Your score point: {weighted_point}')

# if weighted_point >= 20:
# 	st.success("Hurrah! you are eligible for Data Science, Machine Learning Bootcamp")

# else:
# 	st.warning("Try Next time")

