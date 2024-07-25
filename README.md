# agm-website-backend

This Repository is the Backend/API of the website [link]here
It was buit with Django (Pyhton) and has about 6> API endpoints


# API DOCUMENTATION

Sample code linked in this file is a HTML file, the Js script at the end of the <body> tag uses JQuery. Make sure you have the JQuery library linked to the HTML File

Please send a message to me at adegitetaiwo24@gmail.com


Endpoint to get the list of all campus
	Endpoint: https://afcfagm.pythonanywhere.com/api/get-all-campusavs/
               Method: GET

	*Use the above endpoint to fetch all the list of campus Avs (check sample code here)
	
	Success Response looks like this

	"queryset": [
        {
            "id": 1,
            "campusOrSchoolAcronym": "FUTA",
            "campusName": "Federal University of Technology Akure",
     "InstitutionType": "university", // or polytechnic or college
            "about": "This Field is required",
	     "fellowship_facebook_link": null,
	     "fellowship_instagram_link": null,
     "fellowship_email": null,
     "fellowship_phone_number": null,
            "flyer": "https://res.cloudinary.com/drzllgwgm/image/upload/v1/AGM%20Portal%20Media%20Files/campus_avs_images/Fellowship_members_nhraqs",
            "bibleStudyTime": "",
            "bibleStudyVenue": "",
            "fellowshipTime": "",
            "fellowshipVenue": "",
            "OtherScheduleOfServiceDetails": "",
            "averageNumberOfStudent": 50,
            "numberOfWorkforce": 0,
            "joinAlumiGroup": null,
            "coordinator_name": "John Fafure",
            "coordinator_picture": null,
            "coordinator_course": null,
            "coordinator_level": null,
            "coordinator_email": null,
            "coordinator_phonenumber": null,
            "secretary_name": "Deborah Oke",
            "secretary_picture": null,
            "secretary_course": null,
            "secretary_level": null,
            "secretary_email": null,
            "secretary_phonenumber": null,
            "posted": "2024-07-15T22:44:00.128307Z",
            "last_edited": "2024-07-16T22:55:58.649280Z"
        }
    ]

Endpoint to get details of a Specific campus AVS
	Endpoint: https://afcfagm.pythonanywhere.com/api/get-all-campusavs/?campus=${campusAcronym}   
              Method: GET


	NB: The parameter “campus” must be passed and the value should be equal to the campus Acronym of the particular campus Avs that was clicked eg. “FUTA”.  You can get the Acronym from the link that the user clicked. Check Javascript sample code for ideas.
	Use the above endpoint to fetch a specific campus Avs  (check sample code here)


	
To get report of a particular campus

Endpoint: https://afcfagm.pythonanywhere.com/api/get-report/?campus=${campusAcronym}&program-type
=${program_type} 

Method: GET

The Program type value MUST either be “revival_program” OR “welcome_program”

Success Response

{
    "queryset": [
        {
            "id": 1,
            "campusOrSchoolAcronym": "futa",
            "program_type": "welcome_program",
            "year": "",
            "salvation": "",
            "sanctification": "",
            "baptism": "",
            "healing": "",
            "TotalAttendanceMale": "",
            "TotalAttendanceFemale": "",
            "TotalAttendance": "",
            "body": ""
        }
    ]
}



To get images for the reports

	Endpoint: https://afcfagm.pythonanywhere.com/api/get-report-images/?campus=${campusAcronym}&program-type=${program_type} 
	
            Method: GET

The Program type value MUST either be “revival_program” OR “welcome_program”

Success Response

{
    "queryset": [
        {
            "id": 1,
            "campusOrSchoolAcronym": "FUTA",
            "program_type": "revival_program",
            "picture1": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/report_images/Fellowship_members_h46hsm.jpg",
            "picture2": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/report_images/Finished_French_jgppti.png",
            "picture3": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/report_images/Taiwo_Adegite_headshot-removebg-preview_wttlpm.png",
            "picture4": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/report_images/Fellowship_members_aucvml.jpg"
        }
    ]
}

To upload Historical Images for a Specific Campus

	Endpoint: https://afcfagm.pythonanywhere.com/api/add-history-images/
            Method: POST

### Sample JS code
const form = new FormData();
form.append("campusOrSchoolAcronym", campusAcronym);
form.append("picture", picture);

	Parameter to Pass are
	i. campus
	ii. picture
	
	Success Response
	
	{
    		"queryset": {
        		"campusOrSchoolAcronym": "futa",
        		"message": "New Picture, Successfully Uploaded!"
    			}
}


### NB: Make sure to submit the data using FormData in Javascript or Jquery. I have implemented it with JQuery in this sample code

Fetch all the Historical images for a specific Campus
	Endpoint: https://afcfagm.pythonanywhere.com/api/get-history-images/?campus=${campusAcronym} 

            Method: GET

	Success Response

	{
    "queryset": [
        {
            "id": 1,
            "campusOrSchoolAcronym": "futa",
            "picture": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/history_images/1712081403143_qrzymu.jpeg"
        },
        {
            "id": 2,
            "campusOrSchoolAcronym": "futa",
            "picture": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/history_images/1712081403143_jder8m.jpeg"
        },
        {
            "id": 3,
            "campusOrSchoolAcronym": "futa",
            "picture": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/history_images/resagratia_logo_lpvgga.png"
        },
        {
            "id": 4,
            "campusOrSchoolAcronym": "futa",
            "picture": "https://res.cloudinary.com/drzllgwgm/raw/upload/v1/AGM%20Portal%20Media%20Files/history_images/percentages_of_total_due_paid_kddzgf.png"
        }
    ]
}


