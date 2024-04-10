pipeline{
    agent {
        kubernetes {
            defaultContainer 'jnlp'
        }
    }

    stages{

        stage('Deploy to Kubernetes') {
            steps {
                script {
//                     kubernetesDeploy(
//                         configFile: 'deployment.yaml',
//                         kubeconfigId: 'k8s'
//                     )
                     sh "kubectl get ns"
                     sh "kubectl apply -f deployment.yaml"
                }
            }
        }
    }

}
