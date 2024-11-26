/* script.js */

document.getElementById("workingProfessionalOrStudent").addEventListener("change", function() {
    let studySatisfactionField = document.getElementById("studySatisfaction");
    let academicPressureField = document.getElementById("academicPressure");
    let cgpaField = document.getElementById("cgpa");
    let professionField = document.getElementById("profession");
    let workPressureField = document.getElementById("workPressure");
    let jobSatisfactionField = document.getElementById("jobSatisfaction");
    let workingStatus = this.value;
  
    if (workingStatus === "student") {
        professionField.value = "Not Applicable";
        professionField.disabled = true;
        if (workPressureField) {
            workPressureField.value = '-1';
        }
        if (jobSatisfactionField) {
            jobSatisfactionField.value = '-1';
        }
    } else if (workingStatus === "working professional") {
        professionField.disabled = false;
        professionField.value = ""; // Reset value if user changes to working professional
        if (workPressureField) {
            workPressureField.value = "";
        }
        if (jobSatisfactionField) {
            jobSatisfactionField.value = "";
        }
        if (studySatisfactionField) {
            studySatisfactionField.value = '-1';
        }
        if (academicPressureField) {
            academicPressureField.value = '-1';
        }
        if (cgpaField) {
            cgpaField.value = '-1';
        }
    }
});

/* Update professions dropdown in HTML */
let professionSelect = document.getElementById("profession");
if (professionSelect) {
    let professions = [
        "Not Applicable",
        "Software Engineer",
        "Doctor",
        "Teacher",
        "Data Scientist",
        "Lawyer",
        "Accountant",
        "Nurse",
        "Mechanical Engineer",
        "Marketing Manager",
        "Sales Executive",
        "Architect",
        "Civil Engineer",
        "Pharmacist",
        "Graphic Designer",
        "Human Resources Manager",
        "Business Analyst",
        "Electrician",
        "Plumber",
        "UX/UI Designer",
        "Digital Marketer"
    ];

    professions.forEach(function(profession) {
        let option = document.createElement("option");
        option.value = profession;
        option.text = profession;
        professionSelect.appendChild(option);
    });
}

/* Update cities dropdown in HTML */
let citySelect = document.getElementById("city");
if (citySelect) {
    let cities = [
        "Delhi",
        "Mumbai",
        "Bangalore",
        "Hyderabad",
        "Ahmedabad",
        "Chennai",
        "Kolkata",
        "Pune",
        "Jaipur",
        "Lucknow",
        "Kanpur",
        "Nagpur",
        "Indore",
        "Thane",
        "Bhopal",
        "Visakhapatnam",
        "Patna",
        "Vadodara",
        "Ghaziabad",
        "Ludhiana"
    ];

    cities.forEach(function(city) {
        let option = document.createElement("option");
        option.value = city;
        option.text = city;
        citySelect.appendChild(option);
    });
}
