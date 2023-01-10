#install flask from pip3 using flask

package {'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}