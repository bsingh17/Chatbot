## greet
* greet
    - utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null} 
	- utter_suggestion

## thank
* thankyou
	- utter_noworries

## goodbye
* goodbye
	- utter_bye

## FAQ Questions
* faq
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- respond_faq

## path1- a new person directly going for paid course
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye



## path2- a new person opting for free course
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

	
## path3- a new person enquiring for free course but take a paid course
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye		

	
## path4- an existing missionEd customer comes for a free course
* free_course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path5- A person comes to just enquire about the courses offered
* greet
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* price
	- utter_tell_price
* free_course	
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path6- A person coming to enquire about the paid courses
* greet	
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* price
	- utter_tell_price
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path7- new customer comes for free and paid course but didn't took both 
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 


## path8- existing customer comes for free course but didn't took 
* free_course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_free_course_link
* not_interested
    - utter_we_will_come_with_new_courses   
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path9- a new customer going for paid as well as free course too
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path10
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* about_missionED
	- utter_intro_to_MissionEd
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path11
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path12
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path13
* greet
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_product
	- utter_explain_product
* price
	- utter_tell_price
* free_course		
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path 14
* greet	
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_product
	- utter_explain_product
* about_missionED
	- utter_intro_to_MissionEd
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* price
	- utter_tell_price
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 15
* about_product
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path 16

* about_product
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye


	
## short path-1
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short path-2
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short path-3
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye	

## short path-4
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## short story-5
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short story-6
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* about_missionED
	- utter_intro_to_MissionEd
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short story-7
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short story-8
* greet
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_product
	- utter_explain_product
* free_course	
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye	
## short story-9
* greet
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_product
	- utter_explain_product
* about_missionED
	- utter_intro_to_MissionEd
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short story-10
* about_product
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 
	
## path 17
* registration
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 18
* registration
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_registration_link
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path19
* registration
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_registration_link
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path 20
* registration
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_registration_link
* course 
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
	
## path 21
* registration
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_registration_link
* free_course
	- utter_free_course_link
* not_interested
    - utter_we_will_come_with_new_courses   
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path 22
* registration
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 23
* course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## short story 11
* course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
## path 24
* course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 25
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 26

* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* course 
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 27
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 28
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 29
* payment
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 30
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path31
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye	

## path 32
* free_course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_free_course_link
* registration
	- utter_registration_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 33
* greet	
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* registration
	- utter_registration_link
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* price
	- utter_tell_price
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 34
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* registration
	- utter_registration_link
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path 35
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration
	- utter_registration_link
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path 36
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* about_missionED
	- utter_intro_to_MissionEd
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 37
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* registration
	- utter_registration_link
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 38
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* course 
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration
	- utter_registration_link
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 39
* course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* registration
	- utter_registration_link
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 40
* course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration
	- utter_registration_link
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path 41
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* registration
	- utter_registration_link
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 42
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration	
	- utter_registration_link
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 43
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 44
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 45
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* about_product
	- utter_explain_product
* faq
	- respond_faq
* course	
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 46
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 47
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* faq	
	- respond_faq
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye		

## path 48
* greet
	- utter_greet
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_suggestion
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* price
	- utter_tell_price
* free_course	
	- utter_free_course_link
* faq
	- respond_faq
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 49
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* faq	
	- respond_faq
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path 50
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* about_missionED
	- utter_intro_to_MissionEd
* ask_help
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path 51
* about_product	
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* ask_help
	- action_ask_bot
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq	
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path 52
* about_product
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_explain_product
* ask_help
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 53
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq	
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 54
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* registration
	- utter_registration_link
* free_course
	- utter_free_course_link
* faq
	- respond_faq
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 55
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 56
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 57
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 58
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye
	
## path 59
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* registration
	- utter_registration_link
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* faq
	- respond_faq
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye	
	
## path 60
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* registration
	- utter_registration_link
* free_course
	- utter_free_course_link
* not_interested
	- utter_tell_about_paid_courses
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* not_interested
    - utter_we_will_come_with_new_courses
* thankyou
	- utter_noworries
* goodbye
	- utter_bye 

## path 61
* about_missionED
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration
	- utter_registration_link
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 62
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* course 
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration
	- utter_registration_link
* payment	
	- utter_payment_page
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 63
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}	
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* about_missionED
	- utter_intro_to_MissionEd
* about_product
	- utter_explain_product
* registration
	- utter_registration_link
* faq
	- respond_faq
* price
	- utter_tell_price
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye

## path 64
* course
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* ask_help
	- action_ask_bot
* registration
	- utter_registration_link
* price
	- utter_tell_price
* faq
	- respond_faq
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* free_course
	- utter_free_course_link
* thankyou
	- utter_noworries
* goodbye
	- utter_bye


## path 65
* price
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- utter_tell_price
* about_product
	- utter_explain_product
* ask_help
	- action_ask_bot
* course
	- show_courses_form
	- form{"name": "show_courses_form"}
	- form{"name":null}
* registration	
	- utter_registration_link
* payment	
	- utter_payment_page
* payment_confirmation
	- action_payment_done
* thankyou
	- utter_noworries
* goodbye
	- utter_bye






## ask_bot
* ask_help
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
	- action_ask_bot

## bot challenge
* bot_challenge
	- info_form
	- form{"name": "info_form"}
	- form{"name":null}
    - utter_i_am_MissionEd_bot
