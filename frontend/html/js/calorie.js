
$(document).ready(function() {
    var template = `
    <div class="row food">
    <div class="six columns">
    <input class="u-full-width" type="text" placeholder="Enter food">
    </div>
    <button class='remove-food'>Delete</button>
    </div>
    `


    function add_food() {
        $('#food-list').append(template);
    }

    function remove_food() {
        $(this).parent('.food').remove();
    }

    function clear_all() {
        $('#results').children().remove();
        $('form').children().remove();
        add_food();
    }


    function submit() {
        var data = {
            "foods": []
        };
        $('.food-item').each((index, html) => {
            let food = $(html).val();
            if (food) {
                data.foods.push(food);
            }
        });
        console.log('Sending', data);

        $.ajax('/api/v1/calories/', {
            data: JSON.stringify(data),
            contentType: 'application/json',
            type: 'POST',
            success: (result) => {
                let json = JSON.parse(result);
                let output = JSON.stringify(json, undefined, 2);
                $("#results").text(output);
            }
        });
    }


    $('.add-food').click(add_food);
    $('form').submit(function() {return false;});
    $('.clear').click(clear_all);
    $('.calculate').click(submit);
    $(document).on('click', '.remove-food', remove_food);
});

