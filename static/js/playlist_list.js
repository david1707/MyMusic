

$(document).on('click', '.edit-list', (e) => {
    const playlist_id = e.target.id;
  
    $.ajax({
        url: `/playlist/delete/${playlist_id}`
    })
})

$(document).on('click', '.delete-list', (e) => {
    // Remove playlist with id 'playlist_id'
    // If success, remove his <tr>
    const playlist_id = e.target.id;
  
    // Force user to confirm they want to remove the playlist. Else, return
    var remove_prompt = prompt("Please, confirm you want to remove playlist:").toLowerCase();
    if (remove_prompt !== "yes") { return; }

    $.ajax({
        url: `/playlist/delete/${playlist_id}`,
        success: function(data) {
            if (data.status) {
                $(`#playlist-${playlist_id}`).remove();
            }
        },
        error: function(error) {
            alert(`Error: Playlist ${playlist_id} not removed`);
        }

    })
})