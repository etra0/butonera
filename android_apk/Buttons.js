import React from 'react';
import {StyleSheet, Text, View, ScrollView, TouchableOpacity, Button} from 'react-native';


class _Button extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'host': this.props.host,
            'url': this.props.url
        }
    }

    componentDidMount() {
        let name = this.state.url.split(".")
        name.splice(name.length - 1)
        name = name.join("")
        name = name.split("-").join(" ")
        this.setState({name: name});
    }
    
    sendRequest() {
        console.log(this.state.host, this.state.url)
        fetch(`${this.state.host}/play_sound/${this.state.url}`);
    }

    render() {
        console.log(this.state.name)
        return (
            <View style={styles.buttonView}>
                <Text>{this.state.name}</Text>
                <TouchableOpacity
                    onPress={() =>
                        this.sendRequest()
                    }
                    activeOpacity={.5}
                    style={styles.SubmitButtonStyle}
                >
                    <Text> </Text>
                </TouchableOpacity>
            </View>
        )
    }
}


export default class Buttons extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'host': '0.0.0.0',
            'buttons': [],
            'renderable': false
        }
    }

    componentDidMount() {
        const { navigation } = this.props;
        let host = navigation.getParam('host', 'NULL');

        if (!host.startsWith("http")) {
            host = "http://" + host;
        }
        
        this.setState({host: host});
        
        fetch(host + "/get_sounds")
            .then(result => result.json())
            .catch(e => {this.setState({'renderable': false})})
            .then(buttons => { 
                if (buttons)
                    this.setState({'buttons': buttons, 'renderable': true})
                else
                    this.setState({'renderable': false})
            })

    }

    render() {
        let to_render = (
            <ScrollView style={styles.scrollContainer}>
                <View style={styles.buttonContainer}>
                    {this.state.buttons.map((button, index) => { 
                        return <_Button 
                                key={index} 
                                host={this.state.host} 
                                url={button}
                                style={{marginRight: 500}}
                                /> })}
                </View>
            </ScrollView>
        );

        if (this.state.renderable) {
            return to_render
        } else {
            return (
                <View style={styles.container}>
                    <Text>
                        <Text>Al parecer el dominio </Text>
                        <Text style={{fontWeight: 'bold'}}>{this.state.host}</Text>
                        <Text> no es válido</Text>
                    </Text>
                </View>
            );
        }
    }
}

const styles = StyleSheet.create({
    scrollContainer: {
        backgroundColor: '#fff',
        flex: 1
    },
    container: {
        backgroundColor: '#fff',
        flex: 1,
        alignItems: "center",
        justifyContent: 'center'
    },

    buttonContainer: {
        marginTop: 10,
        marginBottom: 10,
        alignItems: 'flex-start',
        flexDirection: "row",
        justifyContent: 'space-around',
        flexWrap: "wrap",
        flex:1
    },
    
    buttonView: {
        width: 180,
        marginBottom: 20,
        alignItems: 'center',
        textAlign: "center"
    },

    SubmitButtonStyle: {
        marginTop: 10,
        paddingTop: 15,
        paddingBottom: 15,
        marginLeft: 30,
        marginRight: 30,
        backgroundColor:'#E56562',
        borderRadius: 50,
        borderWidth: 1,
        width: 50,
        borderColor: '#fff'
      },
});
