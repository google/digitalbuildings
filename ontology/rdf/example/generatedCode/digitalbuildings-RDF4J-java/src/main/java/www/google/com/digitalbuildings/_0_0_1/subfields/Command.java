package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Command 
* The signal given to make an action happen. Defaults to multistate unless given a measurement type
*/
@SuppressWarnings("serial")
public class Command extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ICommand{

	IRI newInstance;
	public Command(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Command"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICommand> getAllCommandsObjectsCreated(){
		Set<ICommand> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Command")).subjects().stream()
		.map(mapper->(ICommand)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}