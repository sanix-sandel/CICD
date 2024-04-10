pipeline{
    agent any
    stages{

        stage('Deploy to Kubernetes') {
            steps {
                script {
//                     kubernetesDeploy(
//                         configFile: 'deployment.yaml',
//                         kubeconfigId: 'k8s'
//                     )
                    sh 'echo $PATH'
                    sh "/opt/homebrew/bin/kubectl get ns"
                    sh "/opt/homebrew/bin/kubectl apply -f deployment.yaml"
                }
            }
        }
    }

}
