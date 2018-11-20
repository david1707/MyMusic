

$(document).on('click', '.edit-list', (e) => {
    const playlist_id = e.target.id;
  
    $.ajax({
        url: `/playlist/delete/${playlist_id}`
    })
})

$(document).on('click', '.delete-list', (e) => {
    const playlist_id = e.target.id;
  
    // Remove playlist with id 'playlist_id'
    // If success, remove his <tr>
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