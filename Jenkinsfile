pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo "Building python application"
                bat "docker build -t myfirstpythonapplication ."
            }
        }
        stage('Run'){
            steps{
                echo "Running python application"
                bat "docker rm mycontainer||exit 0"
                bat "docker run -d -p 5000:5000 --name-mycontainer-myfirstpythonapplication"
            }
        }
        stage('post') {
            success{
                echo "Build is successfully complete"
            }
            failure{
                echo "Build failed. Please check logs"
            }
        }
    }
}
