

function useCachedImage(url) {
  caches.open('my-cache')
  .then(function(cache) {
    // Ищем запрос на изображение в кэше
    cache.match('/static/img/001.jpg')
      .then(function(response) {
        if (response) {
          // Если изображение найдено в кэше, используем его
          var img = document.createElement('img');
          
          img.src = response.url;

          img.style = "border-top-left-radius: .3rem; border-top-right-radius: .3rem;"
          img.classList.add('w-100');
          var id_cashe = document.getElementById('imgcache')

          id_cashe.appendChild(img);

        //   document.body.appendChild(img);
        } else {
          // Если изображение не найдено в кэше, делаем запрос к серверу
          fetch('/static/img/001.jpg')
            .then(function(response) {
              // Клонируем ответ, так как ответ может быть прочитан только один раз
              cache.put('/static/img/001.jpg', response.clone());
              return response;
            })
            .then(function(response) {
              // Используем изображение из ответа
              var img = document.createElement('/static/img/001.jpg');
              img.classList.add('w-100')
              img.src = response.url;
              var id_cashe = document.getElementById('imgcache')
              id_cashe.appendChild(img);
            });
        }
      });
  });

}