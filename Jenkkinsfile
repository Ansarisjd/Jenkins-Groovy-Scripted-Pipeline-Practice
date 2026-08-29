node{
    try{
        stage('checkout'){
            echo "Checking out the code from the repository"
            checkout scm
        }

        stage('show files'){
            ehco "Showing the files in the workspace"
            if(isUnix()){
                sh "ls -ltr"
        }   else{
                bat "dir"
            }
        }
        stage('dependencies installation'){
            ehco "Installing the dependencies"
            if(isUnix()){
                sh "pip install -r requirements.txt"
        }   else{
                bat "pip install -r requirements.txt"
            }
        }
        stage('Run Application'){
            ehco "Running the application"
            if(isUnix()){
                sh "python app.py"
        }   else{
                bat "python app.py"
            }

        stage('Run Tests'){
            ehco "Running the tests"
            if(isUnix()){
                sh "pytest test_app.py"
        }   else{
                bat "pytest test_app.py"
            }

        }

        stage('Build Result'){
            echo "Build and Tests are successful"
        }
        }
    catch(Exception e){
        echo "An error occurred: ${e.getMessage()}"
        currentBuild.result = 'FAILURE'
    }

    finally{
        echo "Cleaning up the workspace"
        deleteDir()
    }
}
