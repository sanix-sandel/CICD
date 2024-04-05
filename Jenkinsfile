pipeline{
    agent any

    environment{
        HELM_HOME = '/charts'
    }

    stages{
        stage("Checkout"){
            steps{
               echo 'Hello WOrlD! Today gonna be lit'
            }
        }

        stage("Deployment"){
            steps{
                script{
                    sh 'kubectl get ns'
                }

            }
        }
    }
}
