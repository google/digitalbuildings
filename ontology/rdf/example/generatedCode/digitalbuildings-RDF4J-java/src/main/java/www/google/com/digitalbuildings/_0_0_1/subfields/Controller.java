package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Controller 
* Control loop, such as a PID controller.
*/
@SuppressWarnings("serial")
public class Controller extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IController{

	IRI newInstance;
	public Controller(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Controller"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IController> getAllControllersObjectsCreated(){
		Set<IController> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Controller")).subjects().stream()
		.map(mapper->(IController)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}