// Function to set all "post-comments" divs to "none" after the page loads
document.addEventListener("DOMContentLoaded", function () {
    hideAllCommentSections();
});

function hideAllCommentSections() {
    const post_comments_list = document.querySelectorAll(".post-comments");
    post_comments_list.forEach(function (post_comments) {
        post_comments.style.display = "none";
    });
}


function commentSectionHandler(index) {
    const post_comments_list = document.querySelectorAll(".post-comments");
    const post_comments = post_comments_list[index];
    toggleCommentSection(post_comments);
}

function toggleCommentSection(post_comments) {
    if (post_comments.style.display === "none") {
        post_comments.style.display = "block";
    } else {
        post_comments.style.display = "none";
    }
}


// Select all elements with the class "comment-section-btn" and store them in an array
const comment_section_btns = document.querySelectorAll(".comment-section-btn");
comment_section_btns.forEach(function (comment_section_btn, index) {
    comment_section_btn.addEventListener("click", function (event) {
        event.preventDefault();
        commentSectionHandler(index);
    });
});
