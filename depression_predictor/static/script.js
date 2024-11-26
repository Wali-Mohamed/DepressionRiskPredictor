/* script.js */

document.getElementById("depressionForm").addEventListener("submit", function(event) {
    let age = document.getElementById("age").value;
    let professionField = document.getElementById("profession");
        let studySatisfactionField = document.getElementById("studySatisfaction");
    let cgpaField = document.getElementById("cgpa");
    let workPressureField = document.getElementById("workPressure");
    let jobSatisfactionField = document.getElementById("jobSatisfaction");

    if (age < 18 || age > 60) {
        alert("Please enter an age between 18 and 60.");
        event.preventDefault();
    }

    if (document.getElementById("workingProfessionalOrStudent").value === "student") {
        professionField.value = "Not Applicable";
        professionField.disabled = true;
        professionField.querySelector("option[value='Not Applicable']").selected = true; // Set the default value explicitly
        if (workPressureField) {
            workPressureField.value = -1;
        }
        if (jobSatisfactionField) {
            jobSatisfactionField.value = -1;
        }
    } else {
        professionField.disabled = false;
        if (studySatisfactionField) {
            studySatisfactionField.value = -1;
        }
        if (cgpaField) {
            cgpaField.value = -1;
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
