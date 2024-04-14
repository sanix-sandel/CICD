pipeline{
    agent any

    parameters {
        text(name: 'YAML_CONTENT', defaultValue: '', description: 'Enter YAML content')
    }

    stages{

        stage('Read YAML file'){
            steps{
                script{
                    def yamlContent = params.YAML_CONTENT
                    echo yamlContent
                    writeFile file: "services.yaml", text: params.YAML_CONTENT
                    release_data = readYaml file: "services.yaml"
                }
            }
        }

        stage('Performing '){
            steps{
                script{
                    release_data.each{release_action, action_data -> echo "${release_action} and  ${action_data}"}
                    def allEnv = getAllEnvironment()
                    allEnv.each { key, value ->
                        echo "${key}: ${value}"
                    }
                }
            }
        }


//         stage('Deploy to Kubernetes') {
//             steps {
//                 script {
//                     sh 'echo $PATH'
//                     sh "/opt/homebrew/bin/kubectl get ns"
//                     sh "/opt/homebrew/bin/kubectl apply -f deployment.yaml"
//                 }
//             }
//         }
//         stage('Pause') {
//             steps {
//                 script {
//                     sleep time: 10, unit: 'SECONDS'
//                 }
//             }
//         }
        stage('Verification'){
            steps{
                script{
                    sh "/opt/homebrew/bin/kubectl get deployment"
                    sh "/opt/homebrew/bin/kubectl describe deployment shopper-deployment"
                }
            }
        }
    }

}
