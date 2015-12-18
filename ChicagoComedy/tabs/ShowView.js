'use strict';

var React = require('react-native');
var {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight
} = React;

var CalendarPicker = require('react-native-calendar-picker');

var showView = React.createClass({
  getInitialState: function() {
    return {
      date: new Date(),
    };
  },
  render: function(){
    var show = this.props.show;
    var imageUrl = 'http://localhost:8080/' + show.imageUrl;
    return (
      <View style={ styles.container }>
        <Image source={{ uri: imageUrl }} style={ styles.cellImage } />
        <Text style={ styles.title }>{ show.title }</Text>
        <Text>Theater: { show.theater }</Text>
        <Text>Description: { show.descrip }</Text>
        <View style={ styles.button }>
          <TouchableHighlight style={ styles.button }>
            <Text>Get Tickets</Text>
          </TouchableHighlight>
        </View>
        <CalendarPicker
          selectedDate = { this.state.date }
          />
      </View>
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 64
  },
  cellImage: {
    height: 300
  },
  title: {
    fontWeight: 'bold'
  },
  buttonRow: {
    alignItems: 'center'
  },
  button: {
    height: 20,
    alignItems: 'center',
  }
});

module.exports = showView;