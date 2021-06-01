a = (() => {
    c(() => {
        for (var t = !1, e = document.getElementsByTagName("tr"), n = 0, a = e.length; n < a; n++) {
            var i = e[n];
            if (i) {
                var g = i.getElementsByTagName("td")[3],
                    c = i.getElementsByTagName("td")[4];
                if (c && g)
                    if ("Chưa trả lời" === c.getElementsByTagName("span")[0].innerText.trim()) {
                        t = !0, g.getElementsByTagName("a")[0].click();
                        break
                    }
            }
        }
        setTimeout(() => window.location.href.includes("phieu-khao-sat-detail") && b(), 1e3), t || alert("Tuyệt vời :))) Bạn đã lươn lẹo hết tất cả khảo sát")
    })
}), b = (() => {
    for (var t = [{
            qt: "Ý kiến khác:",
            qa: "Giảng viên dạy hay, dễ hiểu"
        }, {
            qt: "Khoa",
            qa: "IT - Công nghệ thông tin"
        }, {
            qt: "Về chương trình đào tạo:",
            qa: "Không có ý kiến"
        }, {
            qt: "Về công tác đào tạo:",
            qa: "Không có ý kiến"
        }, {
            qt: "Về công tác hỗ trợ sinh viên:",
            qa: "Không có ý kiến"
        }, {
            qt: "Về hoạt động kết nối và phục vụ cộng đồng:",
            qa: "Không có ý kiến"
        }, {
            qt: "Về cơ sở vật chất:",
            qa: "Không có ý kiến"
        }, {
            qt: "Các ý kiến khác (Phần dành cho SV ghi nhận xét và đề xuất đối với môn học đang được đánh giá)",
            qa: "Không có ý kiến"
        }], e = ["Đồng ý", "3", "Đại học", "ĐH/CĐ chính quy", ">= 70%"], n = /cauhoi(.*)dapan[0-9]/gm, a = document.getElementsByTagName("label"), i = 0, g = a.length; i < g; i++) {
        if ((r = a[i]) && e.includes(r.innerText.trim())) {
            var c = r.getAttribute("for");
            if (m = document.getElementById(c)) {
                var h = m.getAttribute("type");
                null != c && c.match(n) && "radio" === h && r.click()
            }
        }
    }
    var m;
    for (i = 1, g = (m = document.getElementsByTagName("input")).length; i < g; i++) {
        var r;
        if (r = m[i])
            if ("text" === (h = r.getAttribute("type"))) {
                var l = r.parentElement.parentElement.parentElement.getElementsByTagName("tr")[0].getElementsByTagName("td")[0].getElementsByTagName("strong")[0].innerText;
                r.value = t.filter(t => t.qt === l)[0].qa
            }
    }
}), c = (t => {
    for (var e = document.getElementsByTagName("a"), n = !1, a = 1, i = e.length; a < i; a++) {
        var g = e[a];
        if (g) {
            g.getAttribute("type");
            "Xem thêm" === g.innerText.trim() && (g.click(), n = !0, setTimeout(() => c(t), 500))
        }
    }
    n || t()
});
