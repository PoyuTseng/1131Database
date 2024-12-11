// 更新系所選單
function updateDepartments(collegeId, departmentId) {
    const collegeSelect = document.getElementById(collegeId);
    const departmentSelect = document.getElementById(departmentId);

    const departments = {
        "教育學院": ["教育學系", "教育心理與輔導學系", "社會教育學系"],
        "理學院": ["數學系", "物理學系", "化學系"],
        "藝術學院": ["美術學系", "設計學系", "藝術史研究所"],
    };

    const selectedCollege = collegeSelect.value;

    // 清空舊資料
    departmentSelect.innerHTML = "<option value=''>請先選擇學院</option>";

    if (departments[selectedCollege]) {
        departments[selectedCollege].forEach((dept) => {
            const option = document.createElement("option");
            option.value = dept;
            option.textContent = dept;
            departmentSelect.appendChild(option);
        });
    }
}

// 重設表單
function resetForm(formId) {
    document.getElementById(formId).reset();
    updateDepartments("college", "department");
}

// 搜尋課程
function searchCourse(apiEndpoint) {
    const college = document.getElementById("college").value;
    const department = document.getElementById("department").value;

    if (college && department) {
        fetch(`${apiEndpoint}?college=${college}&department=${department}`)
            .then((response) => response.json())
            .then((data) => {
                console.log(data); // 在 console 顯示資料
                // TODO: 在頁面上更新課程資料
            })
            .catch((error) => console.error("Error fetching courses:", error));
    } else {
        alert("請先選擇學院和系所！");
    }
}
