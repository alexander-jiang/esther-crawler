import re
import mechanize
import json

class LoginException(Exception):
    """Exception to be thrown when login to Esther fails."""

def crawler(student_id, password, subjects, course_number):
    ######## LOGIN ########
    br = mechanize.Browser()
    br.open("https://esther.rice.edu/")

    response1 = br.follow_link(text_regex=r"Login")
    print(br.title())
    print(response1.getcode())
    print(response1.geturl())
    # print(response1.info())  # headers
    # print(response1.read())  # body

    br.select_form(name="loginform")
    # print(br.form)
    br.set_value(student_id, name="sid", type="text")
    br.set_value(password, name="PIN", type="password")
    # print(br.find_control(type="submit", nr=0))

    # Login redirects incorrectly (URL query params are in lowercase but they're case sensitive)
    # print(br.click(type="submit", nr=0).get_full_url())
    br.submit(type="submit", nr=0)
    # print(br.title())
    # print(response2.getcode())
    # print(response2.geturl())

    ######## SITE MAP ########
    response3 = br.open("https://esther.rice.edu/selfserve/twbksite.P_DispSiteMap?menu_name_in=bmenu.P_MainMnu&depth_in=2&columns_in=3")
    print(br.title())
    print(response3.getcode())
    if br.title() != "Site Map":
        raise LoginException("Login failed!")
    print(response3.geturl())

    # Click the "show details" button on the site map
    br.select_form(action="/selfserve/twbksite.P_DispSiteMap?menu_name_in=bmenu.P_MainMnu&depth_in=3&columns_in=2")
    # print(br.form)
    response4 = br.submit(name="submitbutton", type="submit")
    # print(br.title())
    # print(response4.getcode())
    # print(response4.geturl())

    ######## ADD/DROP ########
    response5 = br.follow_link(text_regex=r"Add/Drop")
    print(br.title())
    print(response5.getcode())
    print(response5.geturl())

    # Select the registration term (Spring 18)
    br.select_form(action="/selfserve/bwskfreg.P_AltPin")
    # print(br.form)
    br.set_value(["201820"], name="term_in", type="select")
    response6 = br.submit(type="submit", nr=0)
    print(br.title())
    print(response6.getcode())
    print(response6.geturl())

    ######## CLASS SEARCH ########
    br.select_form(action="/selfserve/bwckcoms.P_Regs")
    response7 = br.submit(name="REG_BTN", type="submit", nr=1) # second button is the Class Search button
    print(br.title())
    print(response7.getcode())
    print(response7.geturl())

    br.select_form(action="/selfserve/bwckgens.P_RegsGetCrse")
    response8 = br.submit(name="SUB_BTN", type="submit", nr=1) # second button is the Advanced Search button
    print(br.title())
    print(response8.getcode())
    print(response8.geturl())

    br.select_form(action="/selfserve/bwckgens.P_RegsGetCrse")
    br.set_value(subjects, name="sel_subj", type="select")
    br.set_value(course_number, name="sel_crse", type="text")
    response9 = br.submit(name="sub_btn", type="submit", nr=0)
    print(br.title())
    print(response9.getcode())
    print(response9.geturl())
    print(response9.read())

    ######## LOGOUT ########
    final_response = br.follow_link(text_regex=r"EXIT")
    print(br.title())
    print(final_response.getcode())
    print(final_response.geturl())

def main():
    config_file = open("config.json", "r")
    config_options = json.load(config_file)
    config_file.close()
    student_id = config_options["student_id"]
    password = config_options["password"]
    subjects = config_options["subjects"]
    course_number = config_options["course_number"]
    try:
        crawler(student_id, password, subjects, course_number)
    except LoginException as e:
        print("Couldn't login to Esther! Check the login credentials in config.json or if Esther is down.")

if __name__ == '__main__': main()
