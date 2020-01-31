jQuery.Userinfo = function(username, callback) {
    jQuery.getJSON('https://api.github.com/users/' + username + '/repos?callback=?', callback)
}

jQuery.fn.loadRepos = function(username) {
    var target = this;
    $.Userinfo(username, function(data) {
        var repos = data.data;
        sortByName(repos);    
      
        var list = $('<div uk-scrollspy="target: > div; cls: uk-animation-fade; delay: 500" class="uk-child-width-1-3@s uk-grid-match" uk-grid uk-grid="masonry: true"/>');
        target.empty().append(list);
        $(repos).each(function() {
            if (this.name != (username.toLowerCase() + '.github.com') && this.name != (username.toLowerCase() + '.github.io')) {
                list.append('<div><div style="border-radius:5px; border:1px solid #5bc0de" class="uk-card uk-card-default uk-card-hover uk-card-body"><h3 class="uk-card-title"><a class="uk-link-heading" href="'+ (this.homepage?this.homepage:this.html_url) +'">' + this.name.split('-').join(' ') + '</a></h3><p>' + this.description + '</p></div></div>');
            }
        });      
      });
       
    function sortByName(repos) {
        repos.sort(function(a,b) {
        return a.name - b.name;
       });
    }
};