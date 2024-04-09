pipeline{
    agent {
        kubernetes {

          label 'minikube'

        }
    }

    stages{

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    kubernetesDeploy(
                        configFile: 'deployment.yaml',
                        kubeconfigId: 'k8s'
                    )
//                     sh "kubectl apply -f deployment.yaml"
                }
            }
        }
    }

}
