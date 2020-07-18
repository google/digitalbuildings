package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Remap_required 
*/
@SuppressWarnings("serial")
public class Remap_required extends www.google.com.digitalbuildings._0_0_1.Application implements IRemap_required{

	IRI newInstance;
	public Remap_required(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#Remap_required"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRemap_required> getAllRemap_requiredsObjectsCreated(){
		Set<IRemap_required> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#Remap_required")).subjects().stream()
		.map(mapper->(IRemap_required)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}