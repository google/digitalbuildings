package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Model 
* Particular design version of an asset (e.g. model_label).
*/
@SuppressWarnings("serial")
public class Model extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IModel{

	IRI newInstance;
	public Model(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Model"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IModel> getAllModelsObjectsCreated(){
		Set<IModel> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Model")).subjects().stream()
		.map(mapper->(IModel)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}