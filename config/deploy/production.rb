# server-based syntax
# ======================
# Defines a single server with a list of roles and multiple properties.
# You can define all roles on a single server, or split them:

# server "example.com", user: "deploy", roles: %w{app db web}, my_property: :my_value
# server "example.com", user: "deploy", roles: %w{app web}, other_property: :other_value
# server "db.example.com", user: "deploy", roles: %w{db}

server "bullet.srvz-webapp.he-arc.ch", user: "poweruser", roles: %w{app db web}, port: 1444
set :deploy_to, "/var/www/#{fetch(:application)}"

after 'deploy:publishing', 'django:migrate'

namespace :django do

    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'Apply migrations'
    task :migrate do
        on roles(:web) do |h|
            execute "cp #{shared_path}/.env #{release_path}/backend/BulletDynamics/.env"
            execute "source #{venv_path}/bin/activate && python3 #{release_path}/backend/manage.py migrate && cd #{release_path}/backend &&python3 #{release_path}/backend/manage.py collectstatic --noinput"
	    end
    end
    
end

after 'django:migrate', 'uwsgi:restart'

namespace :uwsgi do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
	        execute :sudo, 'sv reload uwsgi'
	    end
    end
end

after 'deploy:updating', 'python:update_venv'

namespace :python do

    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'update venv'
    task :update_venv do
        on roles([:app, :web]) do |h|
            execute "source #{venv_path}/bin/activate && #{venv_path}/bin/pip install -r #{release_path}/backend/requirements.txt"
        end
    end
end


after 'deploy:publishing', 'frontend:compile'

namespace :frontend do
    desc 'compile frontend'
    task :compile do
        on roles(:web) do |h|
	        execute "cd #{release_path}/frontend && npm install && npm run build"
	    end
    end
end


# role-based syntax
# ==================

# Defines a role with one or multiple servers. The primary server in each
# group is considered to be the first unless any hosts have the primary
# property set. Specify the username and a domain or IP for the server.
# Don't use `:all`, it's a meta role.

# role :app, %w{deploy@example.com}, my_property: :my_value
# role :web, %w{user1@primary.com user2@additional.com}, other_property: :other_value
# role :db,  %w{deploy@example.com}



# Configuration
# =============
# You can set any configuration variable like in config/deploy.rb
# These variables are then only loaded and set in this stage.
# For available Capistrano configuration variables see the documentation page.
# http://capistranorb.com/documentation/getting-started/configuration/
# Feel free to add new variables to customise your setup.



# Custom SSH Options
# ==================
# You may pass any option but keep in mind that net/ssh understands a
# limited set of options, consult the Net::SSH documentation.
# http://net-ssh.github.io/net-ssh/classes/Net/SSH.html#method-c-start
#
# Global options
# --------------
#  set :ssh_options, {
#    keys: %w(/home/user_name/.ssh/id_rsa),
#    forward_agent: false,
#    auth_methods: %w(password)
#  }
#
# The server-based syntax can be used to override options:
# ------------------------------------
# server "example.com",
#   user: "user_name",
#   roles: %w{web app},
#   ssh_options: {
#     user: "user_name", # overrides user setting above
#     keys: %w(/home/user_name/.ssh/id_rsa),
#     forward_agent: false,
#     auth_methods: %w(publickey password)
#     # password: "please use keys"
#   }
