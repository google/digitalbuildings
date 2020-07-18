package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class No_analysis 
*/
@SuppressWarnings("serial")
public class No_analysis extends www.google.com.digitalbuildings._0_0_1.Application implements INo_analysis{

	IRI newInstance;
	public No_analysis(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#No_analysis"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<INo_analysis> getAllNo_analysissObjectsCreated(){
		Set<INo_analysis> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#No_analysis")).subjects().stream()
		.map(mapper->(INo_analysis)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}