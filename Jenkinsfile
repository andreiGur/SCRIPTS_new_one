pipeline {
    agent any

    environment {
        // Define any environment variables you need
        CHROME_DRIVER_VERSION = 'latest'
    }

    stages {
        stage('Setup') {
            steps {
                // Install ChromeDriver and other dependencies
                script {
                    if (isUnix()) {
                        sh '''
                            # Install necessary packages
                            sudo apt-get update
                            sudo apt-get install -y wget unzip python3-pip chromium-browser

                            # Install ChromeDriver
                            CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
                            wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
                            unzip ~/chromedriver_linux64.zip -d ~/
                            sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
                            sudo chown root:root /usr/local/bin/chromedriver
                            sudo chmod 0755 /usr/local/bin/chromedriver

                            # Install Python packages
                            pip3 install selenium requests
                        '''
                    } else {
                        bat '''
                            choco install python
                            pip install selenium requests
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 your_script.py
                        '''
                    } else {
                        bat '''
                            python your_script.py
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up actions, if necessary
            echo 'Cleaning up...'
        }
        success {
            echo 'The script ran successfully!'
        }
        failure {
            echo 'The script failed.'
        }
    }
}
